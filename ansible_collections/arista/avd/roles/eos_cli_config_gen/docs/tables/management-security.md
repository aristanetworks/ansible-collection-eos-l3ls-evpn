<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_security</samp>](## "management_security") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;entropy_sources</samp>](## "management_security.entropy_sources") | Dictionary |  |  |  | Source of entropy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hardware</samp>](## "management_security.entropy_sources.hardware") | Boolean |  |  |  | Use a hardware based source. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;haveged</samp>](## "management_security.entropy_sources.haveged") | Boolean |  |  |  | Use the HAVEGE algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cpu_jitter</samp>](## "management_security.entropy_sources.cpu_jitter") | Boolean |  |  |  | Use the Jitter RNG algorithm of a CPU based source. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hardware_exclusive</samp>](## "management_security.entropy_sources.hardware_exclusive") | Boolean |  |  |  | Only use entropy from the hardware source. |
    | [<samp>&nbsp;&nbsp;password</samp>](## "management_security.password") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;minimum_length</samp>](## "management_security.password.minimum_length") | Integer |  |  | Min: 1<br>Max: 32 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encryption_key_common</samp>](## "management_security.password.encryption_key_common") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encryption_reversible</samp>](## "management_security.password.encryption_reversible") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;policies</samp>](## "management_security.password.policies") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_security.password.policies.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "management_security.password.policies.[].minimum") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;digits</samp>](## "management_security.password.policies.[].minimum.digits") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;length</samp>](## "management_security.password.policies.[].minimum.length") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lower</samp>](## "management_security.password.policies.[].minimum.lower") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;special</samp>](## "management_security.password.policies.[].minimum.special") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;upper</samp>](## "management_security.password.policies.[].minimum.upper") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "management_security.password.policies.[].maximum") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;repetitive</samp>](## "management_security.password.policies.[].maximum.repetitive") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequential</samp>](## "management_security.password.policies.[].maximum.sequential") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;ssl_profiles</samp>](## "management_security.ssl_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_security.ssl_profiles.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fips_restrictions</samp>](## "management_security.ssl_profiles.[].fips_restrictions") | Boolean |  |  |  | Use FIPS compliant algorithms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tls_versions</samp>](## "management_security.ssl_profiles.[].tls_versions") | String |  |  |  | List of allowed TLS versions as string.<br>Examples:<br>  - "1.0"<br>  - "1.0 1.1"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cipher_list</samp>](## "management_security.ssl_profiles.[].cipher_list") | String |  |  |  | cipher_list syntax follows the openssl cipher strings format.<br>Colon (:) separated list of allowed ciphers as a string.<br>Not supported on EOS version starting 4.32.0F, use the `ciphers` setting instead.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ciphers</samp>](## "management_security.ssl_profiles.[].ciphers") | Dictionary |  |  |  | This setting is applicable to EOS versions 4.32.0F and later. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;v1_0</samp>](## "management_security.ssl_profiles.[].ciphers.v1_0") | String |  |  |  | The cipher suites for TLS version 1.0, 1.1 and 1.2.<br>Colon (:) separated list of allowed ciphers as a string.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;v1_3</samp>](## "management_security.ssl_profiles.[].ciphers.v1_3") | String |  |  |  | The cipher suites for TLS version 1.3.<br>Colon (:) separated list of allowed ciphers as a string.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trust_certificate</samp>](## "management_security.ssl_profiles.[].trust_certificate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;certificates</samp>](## "management_security.ssl_profiles.[].trust_certificate.certificates") | List, items: String |  |  |  | List of trust certificate names.<br>Examples:<br>  - test1.crt<br>  - test2.crt<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_security.ssl_profiles.[].trust_certificate.certificates.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;requirement</samp>](## "management_security.ssl_profiles.[].trust_certificate.requirement") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;basic_constraint_ca</samp>](## "management_security.ssl_profiles.[].trust_certificate.requirement.basic_constraint_ca") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hostname_fqdn</samp>](## "management_security.ssl_profiles.[].trust_certificate.requirement.hostname_fqdn") | Boolean |  |  |  | Enforce hostname to be FQDN without wildcard.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policy_expiry_date_ignore</samp>](## "management_security.ssl_profiles.[].trust_certificate.policy_expiry_date_ignore") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system</samp>](## "management_security.ssl_profiles.[].trust_certificate.system") | Boolean |  |  |  | Use system-supplied trust certificates.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chain_certificate</samp>](## "management_security.ssl_profiles.[].chain_certificate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;certificates</samp>](## "management_security.ssl_profiles.[].chain_certificate.certificates") | List, items: String |  |  |  | List of chain certificate names.<br>Examples:<br>  - chain1.crt<br>  - chain2.crt<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_security.ssl_profiles.[].chain_certificate.certificates.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;requirement</samp>](## "management_security.ssl_profiles.[].chain_certificate.requirement") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;basic_constraint_ca</samp>](## "management_security.ssl_profiles.[].chain_certificate.requirement.basic_constraint_ca") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_root_ca</samp>](## "management_security.ssl_profiles.[].chain_certificate.requirement.include_root_ca") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;certificate</samp>](## "management_security.ssl_profiles.[].certificate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;file</samp>](## "management_security.ssl_profiles.[].certificate.file") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "management_security.ssl_profiles.[].certificate.key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;certificate_revocation_lists</samp>](## "management_security.ssl_profiles.[].certificate_revocation_lists") | List, items: String |  |  |  | List of CRLs (Certificate Revocation List).<br>If specified, one CRL needs to be provided for every certificate in the chain, even if the revocation list in the CRL is empty.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_security.ssl_profiles.[].certificate_revocation_lists.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;shared_secret_profiles</samp>](## "management_security.shared_secret_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;profile</samp>](## "management_security.shared_secret_profiles.[].profile") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;secrets</samp>](## "management_security.shared_secret_profiles.[].secrets") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_security.shared_secret_profiles.[].secrets.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;secret</samp>](## "management_security.shared_secret_profiles.[].secrets.[].secret") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;secret_type</samp>](## "management_security.shared_secret_profiles.[].secrets.[].secret_type") | String |  | `7` | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive_lifetime</samp>](## "management_security.shared_secret_profiles.[].secrets.[].receive_lifetime") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;infinite</samp>](## "management_security.shared_secret_profiles.[].secrets.[].receive_lifetime.infinite") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;start_date_time</samp>](## "management_security.shared_secret_profiles.[].secrets.[].receive_lifetime.start_date_time") | String |  |  |  | Start date and time of lifetime of the secret. End date should be greater than start date.<br>Formats supported:<br>1. mm/dd/yyyy hh:mm:ss<br>2. yyyy-mm-dd hh:mm:ss<br>e.g 2024-12-20 10:00:00 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;end_date_time</samp>](## "management_security.shared_secret_profiles.[].secrets.[].receive_lifetime.end_date_time") | String |  |  |  | End date and time of lifetime of the secret. End date should be greater than start date.<br>Formats supported:<br>1. mm/dd/yyyy hh:mm:ss<br>2. yyyy-mm-dd hh:mm:ss<br>e.g 2024-12-20 10:00:00 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transmit_lifetime</samp>](## "management_security.shared_secret_profiles.[].secrets.[].transmit_lifetime") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;infinite</samp>](## "management_security.shared_secret_profiles.[].secrets.[].transmit_lifetime.infinite") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;start_date_time</samp>](## "management_security.shared_secret_profiles.[].secrets.[].transmit_lifetime.start_date_time") | String |  |  |  | Start date and time of lifetime of the secret. End date should be greater than start date.<br>Formats supported:<br>1. mm/dd/yyyy hh:mm:ss<br>2. yyyy-mm-dd hh:mm:ss<br>e.g 2024-12-20 10:00:00 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;end_date_time</samp>](## "management_security.shared_secret_profiles.[].secrets.[].transmit_lifetime.end_date_time") | String |  |  |  | End date and time of lifetime of the secret. End date should be greater than start date.<br>Formats supported:<br>1. mm/dd/yyyy hh:mm:ss<br>2. yyyy-mm-dd hh:mm:ss<br>e.g 2024-12-20 10:00:00 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_time</samp>](## "management_security.shared_secret_profiles.[].secrets.[].local_time") | Boolean |  |  |  | Configuring secret using the local timezone from system clock. Default is UTC. |
    | [<samp>&nbsp;&nbsp;entropy_source</samp>](## "management_security.entropy_source") <span style="color:red">removed</span> | String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version v5.0.0. Use <samp>entropy_sources</samp> instead.</span> |

=== "YAML"

    ```yaml
    management_security:

      # Source of entropy.
      entropy_sources:

        # Use a hardware based source.
        hardware: <bool>

        # Use the HAVEGE algorithm.
        haveged: <bool>

        # Use the Jitter RNG algorithm of a CPU based source.
        cpu_jitter: <bool>

        # Only use entropy from the hardware source.
        hardware_exclusive: <bool>
      password:
        minimum_length: <int; 1-32>
        encryption_key_common: <bool>
        encryption_reversible: <str>
        policies:
          - name: <str; required; unique>
            minimum:
              digits: <int; 1-65535>
              length: <int; 1-65535>
              lower: <int; 1-65535>
              special: <int; 1-65535>
              upper: <int; 1-65535>
            maximum:
              repetitive: <int; 1-65535>
              sequential: <int; 1-65535>
      ssl_profiles:
        - name: <str>

          # Use FIPS compliant algorithms.
          fips_restrictions: <bool>

          # List of allowed TLS versions as string.
          # Examples:
          #   - "1.0"
          #   - "1.0 1.1"
          tls_versions: <str>

          # cipher_list syntax follows the openssl cipher strings format.
          # Colon (:) separated list of allowed ciphers as a string.
          # Not supported on EOS version starting 4.32.0F, use the `ciphers` setting instead.
          cipher_list: <str>

          # This setting is applicable to EOS versions 4.32.0F and later.
          ciphers:

            # The cipher suites for TLS version 1.0, 1.1 and 1.2.
            # Colon (:) separated list of allowed ciphers as a string.
            v1_0: <str>

            # The cipher suites for TLS version 1.3.
            # Colon (:) separated list of allowed ciphers as a string.
            v1_3: <str>
          trust_certificate:

            # List of trust certificate names.
            # Examples:
            #   - test1.crt
            #   - test2.crt
            certificates:
              - <str>
            requirement:
              basic_constraint_ca: <bool>

              # Enforce hostname to be FQDN without wildcard.
              hostname_fqdn: <bool>
            policy_expiry_date_ignore: <bool>

            # Use system-supplied trust certificates.
            system: <bool>
          chain_certificate:

            # List of chain certificate names.
            # Examples:
            #   - chain1.crt
            #   - chain2.crt
            certificates:
              - <str>
            requirement:
              basic_constraint_ca: <bool>
              include_root_ca: <bool>
          certificate:
            file: <str>
            key: <str>

          # List of CRLs (Certificate Revocation List).
          # If specified, one CRL needs to be provided for every certificate in the chain, even if the revocation list in the CRL is empty.
          certificate_revocation_lists:
            - <str>
      shared_secret_profiles:
        - profile: <str; required; unique>
          secrets:
            - name: <str; required; unique>
              secret: <str; required>
              secret_type: <str; "0" | "7" | "8a"; default="7">
              receive_lifetime: # required
                infinite: <bool>

                # Start date and time of lifetime of the secret. End date should be greater than start date.
                # Formats supported:
                # 1. mm/dd/yyyy hh:mm:ss
                # 2. yyyy-mm-dd hh:mm:ss
                # e.g 2024-12-20 10:00:00
                start_date_time: <str>

                # End date and time of lifetime of the secret. End date should be greater than start date.
                # Formats supported:
                # 1. mm/dd/yyyy hh:mm:ss
                # 2. yyyy-mm-dd hh:mm:ss
                # e.g 2024-12-20 10:00:00
                end_date_time: <str>
              transmit_lifetime: # required
                infinite: <bool>

                # Start date and time of lifetime of the secret. End date should be greater than start date.
                # Formats supported:
                # 1. mm/dd/yyyy hh:mm:ss
                # 2. yyyy-mm-dd hh:mm:ss
                # e.g 2024-12-20 10:00:00
                start_date_time: <str>

                # End date and time of lifetime of the secret. End date should be greater than start date.
                # Formats supported:
                # 1. mm/dd/yyyy hh:mm:ss
                # 2. yyyy-mm-dd hh:mm:ss
                # e.g 2024-12-20 10:00:00
                end_date_time: <str>

              # Configuring secret using the local timezone from system clock. Default is UTC.
              local_time: <bool>
    ```
