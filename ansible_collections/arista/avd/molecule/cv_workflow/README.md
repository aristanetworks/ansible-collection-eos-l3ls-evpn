## How to test

NOTE:  Can only be run on aawg-ci tenant.

1. Create a service account token on cvaas
2. Load the token as environment variable on your local machine
3. `bash# export CVAAS_AAWG_CI=<your token here>`
4. `bash# cd avd/ansible_collections/arista/avd`
5. `bash# molecule test -s cv_workflow`
6. You can add the `-- -vvv` option to get extended logs
7. Verify that the molecule test completes without any errors

## Test Suite

1. Use the `cv_workflow` action plugin to deploy configs to CV with the following options
   1. `ws_req_state: submitted`
   2. `cc_requested_state: running`
2. Test strict tags functionality with
   1. `strict_tags: true`
3. Test tags value change
   1. Change the value an already existing tag
4. Dotted hostname
   1. Change hostname of the switch to have dots in it
   2. use `cv_workflow` to deploy configs to CV
