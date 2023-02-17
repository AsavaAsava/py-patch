import typer
import codecs

app = typer.Typer()

def get_meta_data(patch_file):
    old_file = str(patch_file[1]).replace("----------- ","").replace("\r\n","")
    new_file = str(patch_file[2]).replace("+++++++++++ ","").replace("\r\n","")
    line_difference = int(patch_file[3][-3])
    return [old_file,new_file,line_difference]

def open_patch_file(file):
    with codecs.open(file,"rb",'utf-16-le') as patch_file:
        patch = patch_file.readlines()
        n =4
        patch_array = [get_meta_data(patch)]

        while n<len(patch):
            if n == None:
                continue
            else:
                patch_array = patch_array + [[str(patch[n]).replace("Line: ","").replace("\r\n",""),str(patch[n+1]).replace(" - ","").replace("\r",""),str(patch[n+2]).replace(" + ","").replace("\r","")]]
                n=n+3
    return patch_array


def open_file(file):
    with open(file,"r") as edit_file:
        edit = edit_file.readlines()
    return edit



def patch_file(mode,patch_data,write_file):
    if mode == "n":
        original_file = open_file(write_file)
        i = 1
        while i < len(patch_data):
            original_file[int(patch_data[i][0])] = patch_data[i][1]
            i = i+1
        with open(write_file,"w") as output:
            output.writelines(original_file)





@app.command()
def main(my_file_path: str , my_patch_file: str):
        patch_file("n",open_patch_file(str(my_patch_file)),my_file_path)
        typer.echo("File Patched Successfully")


if __name__ == "__main__":
        app()

