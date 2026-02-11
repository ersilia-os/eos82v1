# SMILES-based Transformer Encoder-Decoder

SMILES-based Transformer Encoder-Decoder (SMILES-TED) is an encoder-decoder model pre-trained on a curated dataset of 91 million SMILES samples sourced from PubChem, equivalent to 4 billion molecular tokens. SMI-TED supports various complex tasks, including quantum property prediction, with two main variants (289 M and  8x289 M). SMI Ted has been developed by the IBM.

This model was incorporated on 2025-11-29.Last packaged on 2025-12-24.

## Information
### Identifiers
- **Ersilia Identifier:** `eos82v1`
- **Slug:** `smi-ted`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Embedding`, `Descriptor`, `Chemical language model`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `768`
- **Output Consistency:** `Fixed`
- **Interpretation:** Embedding of the molecule

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feat_000 | float |  | SMI-TED feature 0 of the input molecule |
| feat_001 | float |  | SMI-TED feature 1 of the input molecule |
| feat_002 | float |  | SMI-TED feature 2 of the input molecule |
| feat_003 | float |  | SMI-TED feature 3 of the input molecule |
| feat_004 | float |  | SMI-TED feature 4 of the input molecule |
| feat_005 | float |  | SMI-TED feature 5 of the input molecule |
| feat_006 | float |  | SMI-TED feature 6 of the input molecule |
| feat_007 | float |  | SMI-TED feature 7 of the input molecule |
| feat_008 | float |  | SMI-TED feature 8 of the input molecule |
| feat_009 | float |  | SMI-TED feature 9 of the input molecule |

_10 of 768 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos82v1](https://hub.docker.com/r/ersiliaos/eos82v1)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos82v1.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos82v1.zip)

### Resource Consumption
- **Model Size (Mb):** `1103`
- **Environment Size (Mb):** `1940`
- **Image Size (Mb):** `11117.23`

**Computational Performance (seconds):**
- 10 inputs: `32.62`
- 100 inputs: `32.34`
- 10000 inputs: `710.3`

### References
- **Source Code**: [https://github.com/IBM/materials](https://github.com/IBM/materials)
- **Publication**: [https://www.nature.com/articles/s42004-025-01585-0](https://www.nature.com/articles/s42004-025-01585-0)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2025`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [Apache-2.0](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos82v1
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos82v1
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
