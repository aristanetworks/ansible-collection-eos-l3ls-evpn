#!/bin/bash

USERNAME=$(whoami)
CONTAINER_WORKSPACE=$(git rev-parse --show-toplevel)
CONTAINER_WSF_AVD_PATH=${CONTAINER_WORKSPACE}/ansible_collections/arista/avd

# only install collections if ansible binary is missing
if [ -z "$(command -v ansible)" ]; then

  # if env variables are set - use git
  if ! [ -z "${AVD_GITHUB_REPO}" ] && ! [ -z "${AVD_BRANCH_NAME}" ]; then
    AVD_INSTALL_PATH="git+https://github.com/${AVD_GITHUB_REPO}.git#/ansible_collections/arista/avd/,${AVD_BRANCH_NAME}"
    PYAVD_INSTALL_LOCATION="git+https://github.com/${AVD_GITHUB_REPO}.git@${AVD_BRANCH_NAME}#subdirectory=python-avd"
    pip install "pyavd[ansible] @ ${PYAVD_INSTALL_LOCATION}"
    ansible-galaxy collection install --force ${AVD_INSTALL_PATH}
  # otherwise install requirements and collection from container workspace
  elif [ -f ${CONTAINER_WORKSPACE}/python-avd/pyproject.toml ] && [ -f ${CONTAINER_WSF_AVD_PATH}/requirements-dev.txt ] ; then
    # Install pyavd from source and dev requirements from file
    pip install ${CONTAINER_WORKSPACE}/python-avd[ansible-collection] -r ${CONTAINER_WSF_AVD_PATH}/requirements-dev.txt
    # Install arista.avd collection from source
    ansible-galaxy collection install --force ${CONTAINER_WSF_AVD_PATH}
  fi

  # if ansible installation failed for whatever reason - raise an error
  if [ -z "$(command -v ansible)" ]; then
    echo "ERROR: Failed to install Ansible and collections." >&2
    exit 1
  fi

fi

# Execute command from docker cli if any.
if [ ${@+True} ]; then
  exec "$@"
# Otherwise just enter sh or zsh.
else
  if [ -f "/bin/zsh" ]; then
    exec zsh
  else
    exec sh
  fi
fi
