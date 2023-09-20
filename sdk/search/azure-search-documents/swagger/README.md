### Tag: package-searchservice

``` yaml $(tag) == 'package-searchservice'
input-file:
- https://github.com/Azure/azure-rest-api-specs/tree/main/specification/search/data-plane/Azure.Search/preview/2023-07-01-Preview/searchservice.json
title: SearchServiceClient
namespace: azure.search.documents.indexes
output-folder: ../azure/search/documents/indexes/_generated
```

### Tag: package-searchindex

``` yaml $(tag) == 'package-searchindex'
input-file: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/search/data-plane/Azure.Search/preview/2023-07-01-Preview/searchindex.json
title: SearchIndexClient
namespace: azure.search.documents
output-folder: ../azure/search/documents/_generated
```

### Settings

``` yaml
license-header: MICROSOFT_MIT_NO_VERSION
payload-flattening-threshold: 1
package-name: azure-search-documents
clear-output-folder: true
no-namespace-folders: true
version-tolerant: false
models-mode: msrest
```

### Python multi-client

Generate all API versions currently shipped for this package

``` yaml
batch:
  - tag: package-searchservice
  - tag: package-searchindex
```
