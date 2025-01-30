## Add schema for data model

<!-- Use this PR Title: Feat(eos_cli_config_gen): Add schema for < data_model_key > -->

## Checklist

### Contributor Checklist

- [ ] Create schema fragment matching data model described in README.md and README_v4.0.md
  - README.md is most complete with all keys. README_v4.0 includes partial data models after conversion to lists.
  - Schema fragment path is `roles/eos_cli_config_gen/schemas/schema_fragments/<data_model_key>.schema.yml`.
  - Copy line 1-5 from another schema (comments and outer type:dict).
  - Refer to [schema documentation](https://avd.arista.com/devel/docs/contribution/input-variable-validation.html) for syntax and/or use YAML Lint plugin from Redhat in VSCode.
  - Use `convert_types` on value that could be mixed type or misinterpreted like integers and numeric strings.
- [ ] If the data model has been converted from wildcard dicts:
  - Add `convert_types: ['dict']` to the schema.
  - Remove `convert_dicts` from the `templates/eos/<>.j2` and `templates/documentation/<>.j2` templates.
- [ ] Run `molecule converge -s build_schemas_and_docs` to update schema and documentation.
- [ ] Test by running `molecule converge -s eos_cli_config_gen` and verify no errors or changes to generated configs/docs.

### Reviewer Checklist

- Reviewer 1:
  - [ ] Verify that data model is fully covered in the described schema. Easiest by looking at the generated documentation.
  - [ ] Verify that `convert_dicts` has been removed from templates as applicable.
  - [ ] Verify no changes to configs/docs on any molecule scenario
  - [ ] Verify that CI pass

- Reviewer 2:
  - [ ] Verify that data model is fully covered in the described schema. Easiest by looking at the generated documentation.
  - [ ] Verify that `convert_dicts` has been removed from templates as applicable.
  - [ ] Verify no changes to configs/docs on any molecule scenario
  - [ ] Verify that CI pass
