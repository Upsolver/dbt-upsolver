from connection_options import Connection_options
from copy_options import Copy_options
from target_options import Target_options
from transformation_options import Transformation_options


def write_header(options_header, file):
    file.write(f"\n\n## {options_header}\n\n")
    file.write("| Option | Storage    | Type | Editable | Optional | Description |\n")
    file.write("| --------| --------- | ---- | -------- | -------- | ----------- |\n")

def write_options_to_md(options_category, options_header, file):
    write_header(options_header, file)
    for key_con, value in options_category.items():
        for key, value in value.items():
            formated_description = (' '.join(value.get('description', '').split())).replace('[\\t\\n\\r]+',' ')
            md_file.write(f"| {key} | {key_con} | {value['type']} | {value['editable']} | {value['optional']} | {formated_description} |\n")

def write_copy_options_to_md(options_category, options_header, file):
    file.write(f"\n\n## {options_header}\n\n")
    file.write("| Option | Storage    | Category | Type | Editable | Optional | Description |\n")
    file.write("| -------| ---------- | -------- | -----| -------- | -------- | ----------- |\n")
    count = 0
    for key_con, value_con in options_category.items():
        for key_job, value_job in value_con.items():
                for key, value in value_job.items():
                    formated_description = (' '.join(value.get('description', '').split())).replace('[\\t\\n\\r]+',' ')
                    md_file.write(f"| {key} | {key_con} | {key_job} | {value['type']} | {value['editable']} | {value['optional']} | {formated_description} |\n")

with open('connection_properties.md', 'w') as md_file:
    write_options_to_md(Connection_options, 'Connection options', md_file)
    write_options_to_md(Target_options, 'Target options', md_file)
    write_options_to_md(Transformation_options, 'Transformation options', md_file)
    write_copy_options_to_md(Copy_options, 'Copy options', md_file)


md_file.close()
