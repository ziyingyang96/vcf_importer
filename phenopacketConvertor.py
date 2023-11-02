#this script is for generate phenopacket from metadata for given biosample
import pandas as pd
import yaml


def phenopacketConvertor(meta_file,biosample,schema):
    sex_dict = {"female": {"id": "PATO:0020002", "label": "female genotypic sex"},
                "male": {"id": "PATO:0020001", "label": "male genotypic sex"}}
    meta=pd.read_csv(meta_file)
    index = list(meta[meta["SAMPLE_NAME"]==biosample].index)[0]
    with open(schema, 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
        yaml_data["biosamples"][0]["externalReferences"][0]["id"] = "biosample:"+meta.loc[index,"BIOSAMPLE_ID"]
        yaml_data["id"] = meta.loc[index,"SAMPLE_NAME"]
        yaml_data["individual_id"] = "onekgind-"+meta.loc[index, "SAMPLE_NAME"]
        yaml_data["subject"]["id"] = "onekgind-"+meta.loc[index, "SAMPLE_NAME"]
        yaml_data["subject"]["sex"] = sex_dict[meta.loc[index,"SEX"]]
        print(yaml_data)
        return yaml_data
