---
layout: default
img: dalle1.png
img_link: http://www.statmt.org/book/
title: Homework 1: Multilingual NLP
img2: dalle2.png
img2_link: http://www.statmt.org/nmt-book/
active_tab: main_page
---

Silver Dataset Creation
=======================

One of the major challenges with Multilingual NLP is the lack of resources in languages outside of English. An effective and popular way to deal with this is through "silver" datasets. These are automatically generated using various methods and algorithms from the field that leverage "gold" datasets (frequently available only in English). The goal of this assignment is to learn how to create a silver dataset using statistical word alignment with word-level English gold annotions. To be explicit, "gold" datasets are taken to be ground-truth and normally manually annotated by humans. These are assumed to be correct --- as humanly possible. Silver datasets are synthetically generated and attempt to create labels using automatic methods.

Multilingual Information Extraction
===================================

Information Extraction (IE)

Word-Alignment
==============

We will make use of statistical word-aligners - namely the IBM models ([Brown et al., 1993](https://aclanthology.org/J93-2003.pdf)).