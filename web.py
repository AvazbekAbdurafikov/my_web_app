import streamlit as st
import function

todos = function.get_todos()

def add_todos():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.write_todos(todos)


st.title("My todo App")
st.subheader("This is my todo APP")
st.write("This app increase my productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

a = st.text_input(label=" ", placeholder="add a new todo", on_change=add_todos, key="new_todo")
