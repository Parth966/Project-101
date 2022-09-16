import dropbox
import os

class TransferData:
   def __init__(self,access_token):
      self.access_token = access_token
              
   def upload_file(self,file_from,file_to):
      local_path = "C:\Parth\Visual Studio - Whithat Junior\Python\Project - 101\Capture666.PNG"
      dbx = dropbox.Dropbox(self.access_token)
      for root, dirs, files in os.walk(file_from):
         for name in files:
            print(os.path.join(root,name))
      relative_Path = os.path.relpath(local_path, file_from)      
      dropbox_Path = os.path.join(file_to,relative_Path) 
      with  open(local_path,'rb') as f:
         dbx.file_upload(f.read(), dropbox_Path, mode=WriteMode('overwrite'))  
    
def main():
   access_token = "sl.BPUifQ0E-hmaY1DVj31zSrcTXGDkQf905Rg33Av-SshI-c8_0hAS0S7AE6LjrFuCfvG82lbvrwKuM5vxhXknT2eUj2OI2Y3cddipoKlsv2oqdoB6s_k_ouQVc8cGqtlD120PTPM"
   transferData = TransferData(access_token)
   file_from: input("Enter the file path")
   file_to: input("Enter the full path to upload to dropbox")
   transferData.upload_file(file_from,file_to)
main()