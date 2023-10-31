from vcfConverter import vcfConverter
import json
# cnv
converter = vcfConverter(vcf_file = 'samples/HG00096.cnv.vcf')
beacon_struct = converter.convertVariants(def_file = 'definition/definition_cnv.yaml')

for s in beacon_struct:
    
    print(s)
with open("HG00096.json", "w") as outfile:
    json.dump(beacon_struct, outfile)
# sv 
# converter = vcfConverter(vcf_file = 'samples/HG00096.sv.vcf')
# beacon_struct = converter.convertVariants(def_file = 'definition/definition_sv.yaml')
#
# for s in beacon_struct:
#     print(s)