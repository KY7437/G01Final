{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM97S6/385bVlet7VXUyFmX",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/KY7437/G01Final/blob/main/RealASQuiz.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import random\n",
        "\n",
        "# Quiz questions (with explanation)\n",
        "questions_data = [\n",
        "    {\n",
        "        \"question\": \"Sarah is a 15-year-old girl who sneaks into the library during the day.\",\n",
        "        \"answer\": False,\n",
        "        \"explanation\": \"Sarah sneaks into the library at night, not during the day.\"\n",
        "    },\n",
        "    {\n",
        "        \"question\": \"The library in Willowby is said to be enchanted.\",\n",
        "        \"answer\": True,\n",
        "        \"explanation\": \"The story clearly describes the library as rumored to be enchanted.\"\n",
        "    },\n",
        "    {\n",
        "        \"question\": \"At midnight, the characters in the books come to life and talk.\",\n",
        "        \"answer\": True,\n",
        "        \"explanation\": \"At midnight, the books whisper and characters step out of the pages.\"\n",
        "    },\n",
        "    {\n",
        "        \"question\": \"Sarah met Harry Potter in the Midnight Library.\",\n",
        "        \"answer\": False,\n",
        "        \"explanation\": \"Harry Potter is not mentioned; she met characters like Alice and pirates from Treasure Island.\"\n",
        "    },\n",
        "    {\n",
        "        \"question\": \"The characters return to their pages as dawn approaches.\",\n",
        "        \"answer\": True,\n",
        "        \"explanation\": \"As dawn approaches, the characters return to their pages.\"\n",
        "    }\n",
        "]\n",
        "\n",
        "st.set_page_config(page_title=\"Midnight Library Quiz\")\n",
        "\n",
        "st.title(\"The Midnight Library - True or False Quiz\")\n",
        "st.markdown(\"Decide whether each statement is **True or False** based on the story.\")\n",
        "\n",
        "# Shuffle only once per session\n",
        "if \"shuffled_questions\" not in st.session_state:\n",
        "    st.session_state.shuffled_questions = random.sample(questions_data, len(questions_data))\n",
        "    st.session_state.current_question = 0\n",
        "    st.session_state.answers = [None] * len(questions_data)\n",
        "\n",
        "# Navigation\n",
        "q_index = st.session_state.current_question\n",
        "question = st.session_state.shuffled_questions[q_index]\n",
        "\n",
        "# Display question\n",
        "st.subheader(f\"Question {q_index + 1} of {len(questions_data)}\")\n",
        "st.write(question[\"question\"])\n",
        "\n",
        "# Answer input\n",
        "selected = st.radio(\"Choose your answer:\", [\"True\", \"False\"], index=0 if st.session_state.answers[q_index] is None else (0 if st.session_state.answers[q_index] else 1))\n",
        "\n",
        "if st.button(\"Submit Answer\"):\n",
        "    st.session_state.answers[q_index] = (selected == \"True\")\n",
        "\n",
        "# Feedback\n",
        "if st.session_state.answers[q_index] is not None:\n",
        "    correct = question[\"answer\"]\n",
        "    if st.session_state.answers[q_index] == correct:\n",
        "        st.success(\"Correct!\")\n",
        "    else:\n",
        "        st.error(\"Incorrect.\")\n",
        "    st.info(f\"Explanation: {question['explanation']}\")\n",
        "\n",
        "# Navigation buttons\n",
        "col1, col2, col3 = st.columns(3)\n",
        "\n",
        "with col1:\n",
        "    if st.button(\"Previous\", disabled=(q_index == 0)):\n",
        "        st.session_state.current_question -= 1\n",
        "\n",
        "with col2:\n",
        "    if st.button(\"Next\", disabled=(q_index == len(questions_data) - 1)):\n",
        "        st.session_state.current_question += 1\n",
        "\n",
        "with col3:\n",
        "    if st.button(\"Show Score\"):\n",
        "        correct_count = sum(\n",
        "            1 for i, q in enumerate(st.session_state.shuffled_questions)\n",
        "            if st.session_state.answers[i] == q[\"answer\"]\n",
        "        )\n",
        "        st.success(f\"You scored {correct_count} out of {len(questions_data)}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 397
        },
        "id": "3hxBWNZcvzSF",
        "outputId": "f88128da-164d-4f48-bb35-0005642e3c0e"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'streamlit'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-2-ff8bb5521fdd>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mrandom\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;31m# Quiz questions (with explanation)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m questions_data = [\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    }
  ]
}