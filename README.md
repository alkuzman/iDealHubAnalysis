# Klupps Analysis

The aim of this project is textual analysis of documents. The documents are defined as entitis which have id and list of data entries,
with dedicated weight. One data entry is textual representation with provided content type and id.

<h1>MVP version</h1>
Currently this project is in its early stages and it offers the following analysis:
- Keyword analysis (weighted keyword recommendation for given document)
- Coverage analysis (score of how well one document covers the content of the other document)
- Sneak peek quality analysis (score of how well one document describes the content of the other document)

<h1>Configuration</h1>
You only have to configure 1 required enviroinment property:
<ul>
  <li>
    TOPICS_DIRECTORY (path to the directory)
  </li>
</ul>

If you want you application to be secure:
- APP_SSL_CERTIFICATE (file path)
- APP_SSL_PRIVATE_KEY (file path)

Other properties:
- FLASK_ENV {production, development}
- APP_NAME (name of the application)
- APP_ANALYZER_THREAD_POOL_SIZE (number of threads)

<h1>Authors</h1>
Aleksandar Kuzmanoski, Viki Peeva
