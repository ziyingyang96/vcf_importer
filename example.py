from vcfConverter import vcfConverter
import json
from phenopacketConvertor import phenopacketConvertor
# cnv
converter = vcfConverter(vcf_file = 'samples/HG00096.cnv.vcf')
beacon_struct = converter.convertVariants(def_file = 'definition/definition_cnv_new.yaml')

for s in beacon_struct:

    print(s)
with open("HG00096.json", "w") as outfile:
    json.dump(beacon_struct, outfile)

# import metadata file path, biosample id and phenopacket schema to generate phenopacket json
metadata=phenopacketConvertor("./metadata/all_samples_meta.csv","HG00096",'definition/definition_phenopacket.yaml')
with open("HG00096_meta.json", "w") as outfile:
    json.dump(metadata, outfile)
# sv 
# converter = vcfConverter(vcf_file = 'samples/HG00096.sv.vcf')
# beacon_struct = converter.convertVariants(def_file = 'definition/definition_sv.yaml')
#
# for s in beacon_struct:
#     print(s)