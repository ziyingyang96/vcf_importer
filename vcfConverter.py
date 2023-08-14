import vcf
import yaml
from interStruct import Variant, Sample



# turn VCF data into objects
# functions for converting the VCF data into customized data structures
class vcfConverter:

    def __init__(self, vcf_file):

        vcf_reader = vcf.Reader(open(vcf_file, 'r'))

        # parse samples
        self.samples = {}
        for sample in vcf_reader.samples:
            self.samples[sample] = Sample(name = sample)

        # parse variants and calls
        self.variants = []

        for record in vcf_reader:
            variant = Variant(record.CHROM, 
                              record.POS-1,
                              record.ID, 
                              record.REF, 
                              record.ALT, 
                              record.QUAL, 
                              record.FILTER, 
                              record.INFO)
          

            for call in record.samples:
                variant.CALLS.append({'NAME':call.sample, 'DATA':call.data._asdict()})
            self.variants.append(variant)    


    # convert the VCF data into a data structure described by a definition file.
    def convertVariants(self, def_file):
        with open(def_file, 'r') as fi:
            definition = yaml.load(fi, Loader=yaml.FullLoader)

        struct = []
        for variant in self.variants:
            struct.extend(variant.convertVariant(definition))

        return struct


