### memobird.py


unofficial Python SDK for [memobird](http://www.memobird.cn/)

### Installation

    $ pip install memobird

### Usage

    from memobird import Memobird

    memobird = Memobird('{ak}')
    memobird.setup_device('{device_id}')
    memobird.print_text('text')
    memobird.print_image('/path/to/image.jpg')
