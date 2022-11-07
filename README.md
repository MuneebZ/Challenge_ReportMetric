<h1>Suade Labs Python Challange 2022 – Muneeb Zafar</h1>

<!-- ABOUT THE PROJECT -->

## About The Project

This repo exists as my submission for the Suade Labs Python Challange 2022. Once submitted and received, it will probably become private to protect confidentiality. The details of the challenge can be found in the following section.

<!-- The Challange -->

## The Challange

We are expecting you to deliver your work as a git project, with a README file containing instructions on how to install/run the project.

You should use python 3 and a web framework of your choice, we use Flask but it is okay to use something else.

You will find an archive here https://updates.suade.org/files/data.zip that contains sample data from an imaginary e-shop.

Your task is to create an endpoint that, for a given date, will return a report that will contain the following metrics:

<br>

– The total number of items sold on that day.

– The total number of customers that made an order that day.

– The total amount of discount given that day.

– The average discount rate applied to the items sold that day.

– The average order total for that day

– The total amount of commissions generated that day.

– The average amount of commissions per order for that day.

– The total amount of commissions earned per promotion that day.

<!-- TABLE OF CONTENTS -->
<br>
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>
<br>

<!-- GETTING STARTED -->

## Getting Started

Use the example steps listed below to set up a local copy.

### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/MuneebZ/Challenge_ReportMetric.git
   ```

2. Install the `requirements.txt` file into a virtualenv or your environment of choice

   ```sh
   pip install -r requirements.txt
   ```
   
   Or install the requirments by running the `setup.py` file
   ```sh
   python setup.py install 
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Run the application by typing `python -m flask run` in the integrated terminal to launch the Flask development server. By default, the development server searches for `app.py`. When you use Flask, the following output ought to appear:

```sh
* Serving Flask app "app" (lazy loading)
* Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Once running, follow the url link provided in the terminal, being `http://127.0.0.1:5000/` (or `http://localhost:5000/` also works).

You are greeted with an endpoint that takes a `Date:` as an input via a form. The date range is from `2019-08-01` until `2019-09-29` as there are 60 days in total from the data provided. This can be changed on `line 31` in `forms.html`.

Once you have selected a date, click on submit and below `Results:` you will get the necessary endpoint response in a `JSON` format.

The tests can be run by typing `pytest` in the integrated terminal.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[comment]: <> (1. Fork the Project)

[comment]: <> (2. Create your Feature Branch &#40;`git checkout -b feature/AmazingFeature`&#41;)

[comment]: <> (3. Commit your Changes &#40;`git commit -m 'Add some AmazingFeature'`&#41;)

[comment]: <> (4. Push to the Branch &#40;`git push origin feature/AmazingFeature`&#41;)

[comment]: <> (5. Open a Pull Request)

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- CONTACT -->

## Contact

Muneeb Zafar – muneebzafar@outlook.com

Project Link: [https://github.com/MuneebZ/Challenge_ReportMetric](https://github.com/MuneebZ/Challenge_ReportMetric)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
