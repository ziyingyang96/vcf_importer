from vcfConverter import vcfConverter

# cnv
converter = vcfConverter(vcf_file = 'samples/HG00096.cnv.vcf')
beacon_struct = converter.convertVariants(def_file = 'definition/definition_cnv.yaml')

for s in beacon_struct:
    s['alternateBases'] = str(s['alternateBases'][0]).split('<')[1].split('>')[0]
    print(s)

# sv 
converter = vcfConverter(vcf_file = 'samples/HG00096.sv.vcf')
beacon_struct = converter.convertVariants(def_file = 'definition/definition_sv.yaml')

for s in beacon_struct:
    print(s)