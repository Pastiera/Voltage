#!/bin/bash

SETUP_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

#
# Base package root. All the other releavant folders are relative to this
# location.
#
export VOLTAGE_ROOT=$SETUP_DIR
echo "VOLTAGE_ROOT set to " $VOLTAGE_ROOT

#
# Add the root folder to the $PYTHONPATH so that we can effectively import
# the relevant modules.
#
export PYTHONPATH=$VOLTAGE_ROOT:$PYTHONPATH
echo "PYTHONPATH set to " $PYTHONPATH
