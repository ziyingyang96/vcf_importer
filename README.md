## vcfConverter
Convert a VCF file to a customized data structure. Developed to facilitate data conversion for the Beacon project.

## Usage
The current proto version converts VCF files from the 1k genome project to the Beacon V2 [specification](https://github.com/ga4gh-beacon/specification-v2-default-schemas/blob/master/default_variant_schema.yaml).

User needs to privde a `definition.yaml` file, which describes the mapping of the desired terms and the corresponding VCF values. An example `definition.yaml` is proivded.

## Example
```Python
from vcfConverter import vcfConverter

converter = vcfConverter(vcf_file = 'samples/HG00096.cnv.vcf')
beacon_struct = converter.convertVariants(def_file = 'definition/definition_cnv.yaml')

print(beacon_struct)
```

## Current limitations
- only tested on 1k genome CNV data
- cannot customize VCF imports

## To do
- CLI
- convert samples

Please let me know other desired functions
