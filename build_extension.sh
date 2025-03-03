#!/bin/bash

###############################################################################
# Author:   Stuart Beesley - StuWareSoftSystems 2021
# Purpose:  Build shell script (Mac) to build Python Extensions for Moneydance
#
# NOTE: The Moneydance extension .mxt file is really just a zip / jar file.....
###############################################################################

set -eu

echo
echo
echo @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
echo @@@@ BUILD of FixDownloadedTransactions RUNNING...
echo @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
echo
echo

EXTN_NAME="fix_downloaded_transactions"
MONEYDANCE_DEVKIT="../moneydance-devkit-5.1"
PRIVATE_KEY="${MONEYDANCE_DEVKIT}/src/priv_key"
PUBLIC_KEY="${MONEYDANCE_DEVKIT}/src/pub_key"

echo "Module build for ${EXTN_NAME} running...."

sMXT="s-${EXTN_NAME}.mxt"
ZIP="./${EXTN_NAME}.zip"
EXTN_DIR="."
MXT="${EXTN_DIR}/${EXTN_NAME}.mxt"
META_INFO="${EXTN_DIR}/meta_info.dict"
SCRIPT_INFO="${EXTN_DIR}/script_info.dict"

FM_DIR="com/moneydance/modules/features/${EXTN_NAME}"
ZIP_COMMENT="Quik Sense Software: FixDownloadedTransactions Python Extension for Moneydance (by Scott Maxwell). Please see README.md"

# Relies on "ant genkeys" and various jar files from within the Moneydance devkit

if ! test -f "${EXTN_DIR}/${EXTN_NAME}.py"; then
  echo "ERROR - ${EXTN_NAME}/${EXTN_NAME}.py does not exist!"
  exit 1
fi

if ! test -f "${SCRIPT_INFO}"; then
  echo "ERROR - ${SCRIPT_INFO} does not exist!"
  exit 1
fi

if ! test -f "${META_INFO}"; then
  echo "ERROR - ${META_INFO} does not exist!"
  exit 1
fi

if ! test -f "${PRIVATE_KEY}"; then
  echo "ERROR - Your private key from ant genkeys does not exist!"
  exit 1
fi

if ! test -f "${MONEYDANCE_DEVKIT}/lib/extadmin.jar"; then
  echo "ERROR - extadmin.jar does not exist!"
  exit 1
fi

if ! test -f "${MONEYDANCE_DEVKIT}/lib/moneydance-dev.jar"; then
  echo "ERROR - moneydance-dev.jar does not exist!"
  exit 1
fi

############## START OF EXTENSION BUILD ################################################################################
rm -f "${MXT}"

echo "Checking / creating ${FM_DIR} dir if needed..."
mkdir -v -p "${FM_DIR}"
if [ $? -ne 0 ]; then
  echo "*** MKDIR ${FM_DIR} dir failed??"
  exit 6
fi

echo "Copy meta_info.dict..."
cp "${META_INFO}" "${FM_DIR}/meta_info.dict"
if [ $? -ne 0 ]; then
  echo "*** cp meta_info.dict Failed??"
  exit 6
fi

echo "Zipping *.py into new mxt..."
sed -i '' 's/^INSTALL_EXTENSION = False/INSTALL_EXTENSION = True/' "${EXTN_DIR}/${EXTN_NAME}.py"
zip -j -z "${MXT}" "${EXTN_DIR}"/*.py <<<"${ZIP_COMMENT}"
if [ $? -ne 0 ]; then
  echo zip -j -z "${MXT}" "${EXTN_DIR}/*.py"
  echo "*** zip *.py Failed??"
  exit 7
fi
sed -i '' 's/^INSTALL_EXTENSION = True/INSTALL_EXTENSION = False/' "${EXTN_DIR}/${EXTN_NAME}.py"

shopt -u nullglob

echo "Zipping LICENSE.txt into mxt..."
zip -j "${MXT}" "${EXTN_DIR}"/LICENSE.txt
if [ $? -ne 0 ]; then
  echo "*** zip LICENSE.txt Failed??"
  exit 16
fi

echo "Zipping README.md into mxt..."
zip -j "${MXT}" "./README.md"
if [ $? -ne 0 ]; then
  echo "*** zip README.md Failed??"
  exit 18
fi

echo "Zipping script_info.dict into mxt..."
zip -j "${MXT}" "${SCRIPT_INFO}"
if [ $? -ne 0 ]; then
  echo "*** zip script_info.dict Failed??"
  exit 20
fi

echo "Zipping meta_info.dict into mxt..."
zip -m "${MXT}" "${FM_DIR}/meta_info.dict"
if [ $? -ne 0 ]; then
  echo "*** zip meta_info.dict Failed??"
  exit 21
fi

echo "copying extadmin.jar..."
cp "${MONEYDANCE_DEVKIT}/lib/extadmin.jar" .
if [ $? -ne 0 ]; then
  echo "*** cp extadmin.jar Failed??"
  exit 27
fi

echo "copying moneydance-dev.jar..."
cp "${MONEYDANCE_DEVKIT}/lib/moneydance-dev.jar" .
if [ $? -ne 0 ]; then
  echo "*** cp moneydance-dev.jar Failed??"
  exit 29
fi

echo "copying priv_key..."
cp "${PRIVATE_KEY}" .
if [ $? -ne 0 ]; then
  echo "*** cp priv_key Failed??"
  exit 31
fi

echo "copying pub_key..."
cp "${PUBLIC_KEY}" .
if [ $? -ne 0 ]; then
  echo "*** cp pub_key Failed??"
  exit 33
fi

echo "Removing old signed mxts if they existed..."
rm -f "${EXTN_DIR}/${sMXT}"
#rm -f "./${sMXT}"

echo "Executing java mxt signing routines..."
java -cp extadmin.jar:moneydance-dev.jar com.moneydance.admin.KeyAdmin signextjar priv_key private_key_id "${EXTN_NAME}" "${MXT}"
if [ $? -ne 0 ]; then
  echo java -cp extadmin.jar:moneydance-dev.jar com.moneydance.admin.KeyAdmin signextjar priv_key private_key_id "${EXTN_NAME}" "${MXT}"
  echo "*** Java self-signing of mxt package Failed??"
  exit 37
fi

if ! test -f "${sMXT}"; then
  echo "ERROR - self-signed ${sMXT} does not exist after java signing?"
  exit 39
else
  echo "Adding comments to signed mxt..."
  zip -z "${sMXT}" <<<"${ZIP_COMMENT}"
  if [ $? -ne 0 ]; then
    echo "*** zip add comments to self-signed ${sMXT} Failed??"
    exit 41
  fi
fi

echo "Removing priv_key, pub_key, extadmin.jar, moneydance-dev.jar"
rm priv_key
rm pub_key
rm extadmin.jar
rm moneydance-dev.jar

echo "Listing mxt contents..."
ls -l "${MXT}"

echo "Listing signed mxt contents..."
ls -l "${sMXT}"

echo "Removing non-signed mxt..."
rm "${MXT}"

echo "Moving signed mxt to source directory..."
mv "${sMXT}" "${MXT}"
if [ $? -ne 0 ]; then
  echo "*** mv of self-signed ${sMXT} to ${MXT} Failed??"
  exit 43
fi

if test -f "${MXT}"; then
  echo "Listing signed mxt contents..."
  ls -l "${MXT}"
  unzip -l "${MXT}"
  echo ===================
  echo "FILE ${MXT} has been built..."
else
  echo "@@@@@@@@@@@@@@@@@"
  echo "PROBLEM CREATING ${MXT} ..."
  exit 45
fi

echo "Removing temporary build directories (com/...)... should be empty...."
rm -r com

echo "@ Building final ZIP file for publication..."

echo "Removing old zip file (if it exists)..."
rm -f "${ZIP}"

echo "Creating zip file with README.md..."
zip -j -z "${ZIP}" README.md <<<"${ZIP_COMMENT}"
if [ $? -ne 0 ]; then
  echo "*** final zip of package to ${ZIP} Failed??"
  exit 47
fi

echo "Adding signed mxt file into zip file..."
zip -j -c "${ZIP}" "${MXT}" <<<"${ZIP_COMMENT}"
if [ $? -ne 0 ]; then
  echo "*** final zip of mxt into zip package Failed??"
  exit 55
fi

shopt -s nullglob
echo "Adding LICENSE.txt txt file into zip file..."
zip -j "${ZIP}" LICENSE.txt
if [ $? -ne 0 ]; then
  echo "*** final zip of LICENSE.txt file into zip package Failed??"
  exit 65
fi
shopt -u nullglob

shopt -s nullglob
echo "Adding MoneyDance.csv file into zip file..."
zip -j "${ZIP}" MoneyDance.csv
if [ $? -ne 0 ]; then
  echo "*** final zip of MoneyDance.csv file into zip package Failed??"
  exit 65
fi
shopt -u nullglob

if test -f "${ZIP}"; then
  echo "Listing zip file contents..."
  ls -l "${ZIP}"
  unzip -l "${ZIP}"
  echo ===================
  echo "DISTRIBUTION FILE ${ZIP} has been built..."
else
  echo "@@@@@@@@@@@@@@@@@"
  echo "PROBLEM CREATING FINAL DISTRIBUTION ${ZIP} !"
  exit 67
fi
