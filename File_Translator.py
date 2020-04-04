from translate import Translator

try:
    path=input("Enter File Path(to translate):")
    with open(path) as tfile:
        try:
            lang=input("Enter Language code (to which translation is required) \n/Refer documentation-'https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes' for ISO 639 codes/:")
            trans_obj=Translator(to_lang=lang)
            data=tfile.readlines()
            tdata=[]
            print("Translation:")
            for line in data:
                trans=trans_obj.translate(line)
                tdata.append(trans)
                print(trans)
            try:
                print("...Generating Translation file...")
                with open("translation0.txt","x",encoding="UTF-8") as out:
                    out.writelines(tdata)
            except FileExistsError:
                print("...File Already Exist...")
            except Exception as e:
                print(e)

        except:
            print("Error 11001: Connectivity Error (Can't Load Translator API or Bad Gateway)")
except FileNotFoundError:
    print("Path not found/ Enter correct path and try again! :) /")

