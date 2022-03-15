{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "BOJ-14915-거스름돈.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNZ7GtSVpn3z2vgN3EnAfjq",
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
        "<a href=\"https://colab.research.google.com/github/ohjiae/Algorithm_Study_2022/blob/main/greedy/ohjiae/BOJ_14915_%EA%B1%B0%EC%8A%A4%EB%A6%84%EB%8F%88.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ClmrrJN8cWqj"
      },
      "outputs": [],
      "source": [
        "N=int(input())\n",
        "def cal(N):\n",
        "    if N%5==0: print(N//5)\n",
        "    elif N<10:\n",
        "        if N==1 or N==3: print(-1)\n",
        "        elif N%2==0: print(N//2)\n",
        "        else: print(cal(N-1)-1)\n",
        "if N>=10 : cal(N)\n",
        "elif (N%5)%2==0: print(N//5)+(N%5)//2\n",
        "else: print(N//5)+((N%5)//2)+2"
      ]
    }
  ]
}