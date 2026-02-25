import os
import shutil
import pandas as pd
FOLDERS=["Input","Processing","Output","Archive","Failed"]
def create_folders():
    for folder in FOLDERS:
        if not os.path.exists(folder):
            os.makedirs(folder)
def move_to_processing(file):
    source=os.path.join("Input",file)
    destination=os.path.join("Processing",file)
    shutil.move(source,destination)
    return destination
def process_file(file_path):
    filename=os.path.basename(file_path)
    try:
        df=pd.read_csv(file_path)
        df=df.drop_duplicates()
        df=df.dropna()
        summary = df.groupby("Internship")["Stipend"].mean()
        cleaned_path=os.path.join("Output",f"cleaned_{filename}")
        summary_path=os.path.join("Output",f"summary_{filename}")
        df.to_csv(cleaned_path,index=False)
        summary.to_csv(summary_path)
        shutil.move(file_path,os.path.join("Archive",filename))
        print(f"{filename} processed successfully")
    except Exception as e:
        shutil.move(file_path,os.path.join("Failed",filename))
        print(f"Error processing {filename}: {e}")
def main():
    create_folders()
    for file in os.listdir("Input"):
        if file.endswith(".csv"):
            processing_path=move_to_processing(file)
            process_file(processing_path)
    print("Processing Complete : )")
if __name__=="__main__":
    main()
