import os

def pic_namer(path: str, header: str, name: str, extension: str):
       
# For it to work you need to give it empty folder in path :)

   files = os.listdir(path)
   sorted_lst = []
   if files == []:
      return f"{path}\{header}_{name}_0.{extension}"
   else:
   #beware of edge case where in path folder there are other files with wanted extension that have correct name but aren't neceserially wanted pictures
      for file in files:
         if file.find(f"_{name}_") != -1:
            if x := file.find(f'.{extension}'):
               file = file[:x]
            file = file.split('_')
            sorted_lst.append(file)   
      for indx in range(len(sorted_lst)):
         if sorted_lst[indx][-1].isdigit():
            sorted_lst[indx][-1] = int(sorted_lst[indx][-1])
            
      sorted_lst.sort(key = lambda x: x[-1], reverse = True)
      sol = sorted_lst[0][-1] + 1
      return f"{path}\{header}_{name}_{sol}.{extension}"

      
if __name__ == "__main__":
   path = r"C:\\Users\graeb\OneDrive\Pulpit\inzynierka\datasets\degree_256_hands"
   header = 'A'
   name = 'hand'
   extension = 'jpg'
   pic_namer(path,header,name,extension)
  
   