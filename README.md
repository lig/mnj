[![Join the chat at https://gitter.im/lig/mnj](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/lig/mnj)
[![Gitlab CI Status](https://gitlab.com/lig/mnj/badges/master/pipeline.svg)](https://gitlab.com/lig/mnj/pipelines)


# Mnj

![Mnj Logo](logo150.png)

⚠️ **WARNING** `master` branch is undergoing development, docs could be outdated.

**Mnj** (_Mongo Energy_) is a helper library to simplify PyMongo interaction


## Install

Install from PyPI

```shell
pip install mnj
```

or to install the latest relatively stable development snapshot

```shell
pip install --pre mnj
```

or clone this repository to get the latest source and invoke install

```shell
python setup.py install
```


## Features

* Using `nj.q` object for constructing queries will help to validate them.
* No creepy `'$op'` strings any more use `op_()` style operators.

Read the [Mnj Docs](http://mnj.readthedocs.io/) to find out more. 
