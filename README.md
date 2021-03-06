# Support for WaveDrom in Python Markdown

This extension adds support for [WaveDrom](https://wavedrom.com/) to
[Python Markdown](https://python-markdown.github.io/).

## Installation

```
pip install markdown-wavedrom
```

This extension parses Markdown and replaces matching sections with HTML script elements.
To enable WaveDrom rendering, you must ensure that the proper JavaScript code is loaded into your
HTML page. See [the WaveDrom documentation](https://github.com/wavedrom/wavedrom#web-usage) for
details.

## Example

```markdown
# My Markdown Documentation

wavedrom (
    { signal: [{ name: "Alfa", wave: "01.zx=ud.23.456789" }] }
)
```

## MkDocs Integration
The following minimal config is required to get markdown-wavedrom to work in MkDocs.

```yaml
markdown_extensions:
  - markdown_wavedrom

extra_javascript:
  - https://cdnjs.cloudflare.com/ajax/libs/wavedrom/2.6.8/wavedrom.min.js
  - https://cdnjs.cloudflare.com/ajax/libs/wavedrom/2.6.8/skins/default.js
  - js/wavedrom_loader.js
```

Where `docs/js/wavedrom_loader.js` has the following content:
```js
window.addEventListener("load", function () {
  WaveDrom.ProcessAll();
});
```

You can of cause also host the WaveDrom JavaScript files locally with your documentation.

For a complete example with MkDocs, see [the markdown-wavedrom-mkdocs-example GitHub page](https://maximiliankoestler.github.io/markdown-wavedrom-mkdocs-example/).

## Development

Feel free to open an issue or a PR if there is something that can be improved.

Releases on PyPI are created automatically through `python-semantic-release`.
Therefore, this project uses [Angular commit message style](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits)
for commits.

### Testing

```
$ pip install -r dev-requirements.txt
$ tox
```
