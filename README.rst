===============================================
mlbench: Distributed Machine Learning Benchmark
===============================================

.. image:: https://travis-ci.com/mlbench/mlbench-core.svg?branch=develop
    :target: https://travis-ci.com/mlbench/mlbench-core

.. image:: https://travis-ci.com/mlbench/mlbench-dashboard.svg?branch=develop
    :target: https://travis-ci.com/mlbench/mlbench-dashboard

.. image:: https://travis-ci.com/mlbench/mlbench-helm.svg?branch=develop
    :target: https://travis-ci.com/mlbench/mlbench-helm

.. image:: https://travis-ci.com/mlbench/mlbench-benchmarks.svg?branch=develop
    :target: https://travis-ci.com/mlbench/mlbench-benchmarks

.. image:: https://readthedocs.org/projects/mlbench/badge/?version=latest
        :target: https://mlbench.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




A public and reproducible collection of reference implementations and benchmark suite for distributed machine learning algorithms, frameworks and systems.


* Project website: https://mlbench.github.io/
* Free software: Apache Software License 2.0
* Documentation: https://mlbench.readthedocs.io.


Features
--------

* For reproducibility and simplicity, we currently focus on standard **supervised ML**, including standard deep learning tasks as well as classic linear ML models.
* We provide **reference implementations** for each algorithm, to make it easy to port to a new framework.
* Our goal is to benchmark all/most currently relevant **distributed execution frameworks**. We welcome contributions of new frameworks in the benchmark suite.
* We provide **precisely defined tasks** and datasets to have a fair and precise comparison of all algorithms, frameworks and hardware.
* Independently of all solver implementations, we provide universal **evaluation code** allowing to compare the result metrics of different solvers and frameworks.
* Our benchmark code is easy to run on **public clouds**.


Repositories
------------
MLBench consists of 5 Github repositories:

* Documentation: http://github.com/mlbench/mlbench-docs
* Helm Charts for Kubernetes: http://github.com/mlbench/mlbench-helm
* Python Core Library: http://github.com/mlbench/mlbench-core
* Closed-Division Benchmark Implementations: http://github.com/mlbench/mlbench-benchmarks
* Dashboard: http://github.com/mlbench/mlbench-dashboard


Community
---------

About us: See :doc:`Authors </authors>`

Mailing list: https://groups.google.com/d/forum/mlbench

Contact Email: mlbench-contact@googlegroups.com
