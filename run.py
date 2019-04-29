from flask import Flask, jsonify, render_template
import csv
import pandas as pd
import numpy as np

app=Flask(__name__)


if __name__=='__main__':
    app.run(debug=True)
