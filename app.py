{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPHMPeF0P+kCmVgewA1CCzw",
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
        "<a href=\"https://colab.research.google.com/github/fabiosilva2022/Curriculum/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "KJAiwuF8y8Lj"
      },
      "outputs": [],
      "source": [
        "# Aplicação Streamlit para classificar novas imagens\n",
        "import streamlit as st\n",
        "from PIL import Image\n",
        "import numpy as np\n",
        "\n",
        "# Título da aplicação\n",
        "st.title(\"Classificador de Gatos e Cachorros\")\n",
        "\n",
        "# Upload de imagem pelo usuário\n",
        "uploaded_file = st.file_uploader(\"Escolha uma imagem...\", type=[\"jpg\", \"jpeg\", \"png\"])\n",
        "\n",
        "if uploaded_file is not None:\n",
        "    # Exibir a imagem carregada\n",
        "    image = Image.open(uploaded_file)\n",
        "    st.image(image, caption=\"Imagem carregada\", use_column_width=True)\n",
        "\n",
        "    # Pré-processar a imagem\n",
        "    img = np.array(image.resize((128, 128))) / 255.0\n",
        "    img = np.expand_dims(img, axis=0)\n",
        "\n",
        "    # Carregar o modelo salvo e fazer predição\n",
        "    model = keras.models.load_model(\"modelo_cachorro_gato.h5\")\n",
        "    prediction = model.predict(img)[0][0]\n",
        "\n",
        "    # Decidir a classe\n",
        "    classes = [\"Gato\", \"Cachorro\"]\n",
        "    predicted_class = classes[int(prediction > 0.5)]\n",
        "\n",
        "    # Exibir o resultado\n",
        "    st.write(f\"Resultado da classificação: **{predicted_class}**\")\n"
      ]
    }
  ]
}