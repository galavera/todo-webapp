import streamlit as st
from functions import *

todos = get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    write_todos(todos)


st.title("Todo App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="-", placeholder="Add new todo...", on_change=add_todo,
              key='new_todo', label_visibility=False)

