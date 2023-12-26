import json

## 파일 상대 경로 이슈 있으면, vscode 디버그 내 launch.json 파일 만들기 이슈임
## "configuration" 내
#  "cwd": "${fileDirname}" 
## 추가하면 됌
with open("test_data.json", "r") as f:
    data = json.load(f)

print(data)

x = [i[0] for i in data["shapes"][0]["points"]]
y = [i[1] for i in data["shapes"][0]["points"]]

min_answer = f"가장 작은 값: X: {min(x)}, Y: {min(y)}"
max_answer = f"가장 큰 값: X: {max(x)}, Y: {max(y)}"
output = min_answer + "\n" + max_answer

print(min_answer)
print(max_answer)

file = open("output.txt", "w")
file.write(output)
file.close()

print(data["file_attributes"]["step"])
print(data["file_attributes"]["DateTimeOriginal"])


