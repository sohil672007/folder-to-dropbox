import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_folder(self,folder_from,folder_to):
        dbx =dropbox.Dropbox(self.access_token)

        f = open(folder_from,'rb')
        dbx._upload(f.read(),folder_to)

def main():
    access_token = '1XTpb02It8cAAAAAAAAAAY2CAGRVfiqn4mseRygCrtw_ztaAeapCuYueODAqJujf'
    transferData = TransferData(access_token)

    folder_from = input("Enter The folder To Transferr :-  ")
    folder_to = input("Enter the path to upload :-  ")

    transferData.upload_file(folder_from, folder_to)
    print("folder has been moved")

main()