import json

def load_data():
    try:
        with open ("youyube.txt", "r") as  file:
            test = json.load(file)
            #print(type(test))
            return test
    except FileNotFoundError:
        return [] #it will load all data in the videos array if available
        
def save_data_helper(videos):
    with open ("youyube.txt", "w") as file:
        json.dump(videos, file) #it will save incoming video json  to the text file 

def list_all_videos(videos):
    for index, video in enumerate(videos,start=1):
        print("\n")
        print(f"{index}. {video['name']}, Duration: {video['time']} \n")

def add_video(videos):
    name = input("enter video name: ")
    time = input("enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("enter video number to be deleted!\n"))

    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("invalid index entered!\n")

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("enter the video number to update \n"))
    if 1 <= index <= len(videos):
        name = input("enter the new video name")
        time = input("enter the new video time")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("invalid index selected! \n")


def main():
    videos = load_data()
    while True:
        print("Enter your choice in Youtube manager : \n")
        print("1) List all your videos : \n")
        print("2) Add a youtube videos : \n")
        print("3) Remove a youtube videos : \n")
        print("4) Update a youtbue video details : \n")
        print("5) Exit the app : \n")
        choice = input("enter your choice : \n") #take input in the format of string
        #print(videos)

        match choice: #list of choice
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                delete_videos(videos)
            case "4":
                update_videos(videos)
            case "5":
                break
            case _:
                print("Invalid choice ! \n") 
if __name__ == "__main__": #it's mean if found main method then call it.
    main()