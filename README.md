# Sample Record Generator

To replicate the spirit of work I did elsewhere, this generates a flat file that roughly symbolizes real data.

## Learning process

- After I created the first version of this script, the major bottleneck was find_int_gaps()
  - v2: find_int_gaps(number_tracking: list, position: int) -> int
    - It's purpose is to look for the next highest number available in the list (list is prepopulated randomly) - further down in the script a number is inserted into that available space.
    - Initial issue: The script was taking upwards of 270 seconds just to generate 30,000 records. When printing out process it was clear that the process became progressivly slower as the list got bigger.
      - First try: I wasn't searching over the actual numbers in the list, I was searching over index positions, which means that results were *completely* off. That was just an accuracy issue though. Using the position to first find the index position of a specific number to begin iterating upward didn't have much impact on performance.
      - Second try: I flipped the if/else statement, which improved performance about 15%, but not nearly the increase I was looking for.
  - v2: find_int_gaps(number_tracking: dict, position: int) -> int
    - I decided to try a dictionary, because of it's location finding performance. This seemed off, since I was only interested in the keys, but I figured it would be far better than iterating over an growing list.
    - Since I was only interested in the keys, I set each key with a dummy value.
    - There was no competition between the performance of using a dictionary vs a list. The 30,000 records were generated in a few seconds.
  - v3: find_int_gaps(number_tracking: set, position: int) -> int
    - Since the dictionary worked so well I figured there must be some type of object that is purpose built for this (without having to resort to dumb values)
    - Searching stackoverflow I found set(). This was a perfect example of the power of searching when you know exactly what you are looking for (rather than just copying and pasting code without understanding it)
    - I updated find_int_gaps to use a set(), tested, and found the performance to be comparable. (I had used cProfile to test differences up to this point, but didn't run it to compare here, because it was just so incredibly fast, like the dctionary)
    - I upped the number of generated records to 1,000,000 and the script finished in 14 seconds (as opposed to 270 for 30,000 when using a list).

## Generator performance

```cmd
pip install snakeviz
python -m cProfile -o temp.dat generate_sample_audit_data.py
snakeviz temp.dat
```
