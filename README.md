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

### Advanced Usage

In case you need more control of contents layout:

    from memobird import Memobird

    memobird = Memobird('{ak}')
    memobird.setup_device('{device_id}')
    
    paper = Paper()
    paper.add_text('text')
    paper.add_text('another text')
    paper.add_image('/path/to/image.jpg')
    paper.add_text('one more text')
    
    paper_id = memobird.print_paper(paper)
    
    // check if paper is printed
    print memobird.is_paper_printed(paper_id)
