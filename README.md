<h1>Flask Product Analytics Report</h1>

<!-- ABOUT THE PROJECT -->

## About The Project

This repo exists as a personal project to combine the Python pandas and flask module into a working project. Using sample data from a ficitonal e-shop, we create report metrics that we would like to output to an endpoint via JSON format for a given date. We want our enpoint report to have the folllowing metrics:

– The total number of customers on a given day.

– The total amount of the day's discounts.

– The total quantity of items sold on a given day.

– The day's average order total

– The total commissions earned on a given day.

– The average commission rate per order on a given day.

– The total commissions received that day for each promotion.

More details about the project can be found below.

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

Use the steps listed below to set up a local copy.

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

Once you have selected a date, click on submit and below `Results:` you will get the necessary endpoint response in a `JSON` format. The promotion ids 1 – 5 are from Google Ads, Organics Google, Organic DuckDuckGo, DuckDuckGo Ads, Bing respectively.

The tests can be run by typing `pytest` in the integrated terminal.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[comment]: <> (1. Fork the Project)

[comment]: <> (2. Create your Feature Branch &#40;`git checkout -b `&#41;)

[comment]: <> (3. Commit your Changes &#40;`git commit -m `&#41;)

[comment]: <> (4. Push to the Branch &#40;`git push origin `&#41;)

[comment]: <> (5. Open a Pull Request)

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- CONTACT -->

## Contact

Muneeb Zafar – muneeb-zafar@outlook.com

Project Link: [https://github.com/MuneebZ/Challenge_ReportMetric](https://github.com/MuneebZ/Challenge_ReportMetric)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
