import streamlit as st
import functions
import os

if not os.path.exists("todo.txt"):
    with open("todo.txt", "w") as file:
        pass
todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title("My Todo App")
st.subheader("This my todo app.")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new to do...",on_change=add_todo, key="new_todo")
# if new_todo:
#     todos.append(new_todo+"\n")
#     functions.write_todos(todos)
#     st.experimental_rerun()

print("Hello")

