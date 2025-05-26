{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOouOWpZ2EJhL/acYZXdJXT",
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
        "<a href=\"https://colab.research.google.com/github/KY7437/G01Final/blob/main/SAQuiz.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import random\n",
        "\n",
        "# 문장 리스트\n",
        "sentences = [\n",
        "    \"The hospital that was built last year is next to my house.\",\n",
        "    \"I received a gift from a chef who was clearly intelligent.\",\n",
        "    \"The machine which used to lie can be abandoned.\",\n",
        "    \"The report was written by the marketing team last week.\",\n",
        "    \"When will your package be delivered to our company?\",\n",
        "    \"There stood an old library that was rumored to be enchanted.\"\n",
        "]\n",
        "\n",
        "# 상태 저장 (Streamlit Session State)\n",
        "if 'index' not in st.session_state:\n",
        "    random.shuffle(sentences)\n",
        "    st.session_state.sentences = sentences\n",
        "    st.session_state.index = 0\n",
        "    st.session_state.score = 0\n",
        "    st.session_state.answers = [''] * len(sentences)\n",
        "    st.session_state.checked = [False] * len(sentences)\n",
        "\n",
        "index = st.session_state.index\n",
        "sentence = st.session_state.sentences[index]\n",
        "correct_words = sentence.strip(\".?\").split()\n",
        "\n",
        "# 섞인 단어는 문제별로 항상 동일하게 유지\n",
        "random.seed(index)\n",
        "shuffled_words = correct_words[:]\n",
        "random.shuffle(shuffled_words)\n",
        "\n",
        "st.title(\"Sentence Ordering Quiz\")\n",
        "st.markdown(f\"### Question {index + 1} of {len(sentences)}\")\n",
        "st.markdown(\"Arrange the following words into a correct sentence:\")\n",
        "st.markdown(\"**\" + \" | \".join(shuffled_words) + \"**\")\n",
        "\n",
        "# 사용자 입력\n",
        "user_input = st.text_input(\"Your answer:\", value=st.session_state.answers[index])\n",
        "\n",
        "# 정답 확인\n",
        "if st.button(\"Check Answer\"):\n",
        "    st.session_state.answers[index] = user_input\n",
        "    normalized_user = user_input.strip(\".? \").lower()\n",
        "    normalized_correct = \" \".join(correct_words).lower()\n",
        "\n",
        "    if normalized_user == normalized_correct:\n",
        "        if not st.session_state.checked[index]:\n",
        "            st.session_state.score += 1\n",
        "            st.session_state.checked[index] = True\n",
        "        st.success(\"Correct!\")\n",
        "    else:\n",
        "        st.error(\"Incorrect.\")\n",
        "        st.info(f\"Correct Answer: {sentence}\")\n",
        "\n",
        "# 점수 및 네비게이션\n",
        "col1, col2, col3 = st.columns(3)\n",
        "\n",
        "with col1:\n",
        "    if st.button(\"Previous\") and index > 0:\n",
        "        st.session_state.index -= 1\n",
        "\n",
        "with col2:\n",
        "    st.markdown(f\"**Score: {st.session_state.score} / {len(sentences)}**\")\n",
        "\n",
        "with col3:\n",
        "    if st.button(\"Next\") and index < len(sentences) - 1:\n",
        "        st.session_state.index += 1"
      ],
      "metadata": {
        "id": "f3UC1b2qxzVu",
        "outputId": "1ccb6139-f035-40e1-ed29-88be82d20237",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 397
        }
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'streamlit'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-4-0c3810a11cf2>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mrandom\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;31m# 문장 리스트\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m sentences = [\n",
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