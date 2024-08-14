import json
# Configuration

font="Arial"
course_fontsize = 16
credit_fontsize = 17
class_styles = {
    "math": 'fillcolor="#FFF2CC", color="#916f0c"',
    "cs": 'fillcolor="#d6ddff", color="#0D32B2"',
    "elective": 'fillcolor="#f0f0f0", color="black"'
}
edgecolor = 'gray'

def generate_graphviz(courses, dependencies):
    print("digraph CS_Course_Dependencies {")
    print("    rankdir=TD;")

    # print("   label=\"CS Course Dependencies\";")
    # print(f"   fontname=\"{font}\";")
    # print("   tooltip=\" \" ;")
    # print("   URL=\"https://github.com/adielBm/cs-course-dependencies\" ;")
    # print(f"node [ URL=\"https://academic.openu.ac.il/cs/computer/program/AF.aspx\", shape=plaintext, fontname=\"{font}\", fontsize=22];    \"CS Course Dependencies\" [label=\"מדעי המחשב\", fontname=\"{font}\", fontsize=50];")

    print(f"    node [shape=box, style=\"filled\",fontname=\"{font}\" , fontsize={course_fontsize}];")
    print(f"    edge [color=\"{edgecolor}\", penwidth=1];")

    # Nodes (courses)
    current_class = None
    for course in courses:
        if course['class'] != current_class:
            current_class = course['class']
            print(f"\n    // {current_class.capitalize()} courses")
            print(f"    node [{class_styles[current_class]}, shape=record];")

        label = f"{course['name']}| <font POINT-SIZE=\"{credit_fontsize}\"><b>{course['credit']}</b></font>"
        url = f"https://www.openu.ac.il/courses/{course['id']}.htm"
        print(f'    "{course["id"]}" [tooltip="{course["id"]}" label=<{label}>, URL="{url}"];')
    

    # Edges (dependencies)
    for dependency in dependencies:
        print(f'    "{dependency[0]}" -> "{dependency[1]}";')

    print("}")

# Load the JSON data
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Generate the Graphviz code
generate_graphviz(data['courses'], data['dependencies'])
