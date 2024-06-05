# Fair or Fare? Understanding Automated Transcription Error Bias in Social Media and Videoconferencing Platforms

This GitHub repository houses supplementary materials for the research paper entitled "Fair or Fare? Understanding Automated Transcription Error Bias in Social Media and Videoconferencing Platforms." 
This work was presented at the 18th AAAI International Conference on Web and Social Media (ICWSM'24).

## Paper Overview
**Authors:** Daniel J. Dubois, Northeastern University; Nicole Holliday, Pomona College; Kaveh Waddell, Consumer Reports and Stanford University; David Choffnes, Northeastern University.

**Paper DOI:** [10.1609/icwsm.v18i1.31320](https://doi.org/10.1609/icwsm.v18i1.31320)

### Abstract
As remote work and learning increases in popularity, individuals, especially those with hearing impairments or who speak English as a second language, may depend on automated transcriptions to participate in business, school, entertainment, or basic communication. In this work, we investigate the automated transcription accuracy of seven popular social media and videoconferencing platforms with respect to some personal characteristics of their users, including gender, age, race, first language, speech rate, F0 frequency, and speech readability. We performed this investigation on a new corpus of 194 hours of English monologues by 846 TED talk speakers. Our results show the presence of significant bias, with transcripts less accurate for speakers that are male or non-native English speakers. We also observe differences in accuracy among platforms for different types of speakers. These results indicate that, while platforms have improved their automatic captioning, much work remains to make captions accessible for a wider variety of speakers and listeners.

### Bibtex Citation
    @inproceedings{dubois-icwsm24,
        title={{Fair or Fare? Understanding Automated Transcription Error Bias in Social Mediaand Videoconferencing Platforms}},
        author={Dubois, Daniel J. and Holliday, Nicole and Waddell, Kaveh and Choffnes, David},
        booktitle={Proc. of the 18th International AAAI Conference on Web and Social Media (ICSWSM'24)},
        year={2024}
	}

## Dataset

### MonoTED Corpus
- **Description:** This corpus consists of audio and ground-truth transcripts from 846 TED talks, representing 194 hours and over 1.8 million words of spoken content. The talks are all monologues by different speakers.
- **Metadata:** Each talk is annotated with the speaker’s age at the time of the talk, perceived gender, perceived race, English language status (L2 for non-native English speakers), speech rate (words per second), and the fundamental frequency of their voice (F0), including both mean and median values.
- **Access Link:** [Download MonoTED Corpus](https://www.dropbox.com/scl/fi/2fujwuor01w5otjnwa67c/MonoTED.zip?rlkey=sebwtabqnuwtirmwi7m92z7bm&dl=0)
- **License:** Creative Commons CC BY–NC–ND 4.0 International.

### Additional Resources
- **platform-generated-transcripts.zip**
  - Archive containing the transcripts generated during our experiments organized by platform (abbreviations used: YT for YouTube, MS for Microsoft Stream, FB for Facebook Video, ZM for Zoom, BJ for BlueJeans, GM for Google Meet, WX for WebEX).
- **wer.csv**
  - CSV files that includes word error rates (WER) for each talk across each platform, along with metadata such as speaker details and speech characteristics from the MonoTED corpus.
- **calc_wer.py**
  - A Python script that computes the word error rate (WER) using the JiWER library, requiring two inputs: the path to the ground-truth transcript and the path to the hypothesis transcript.
  - Further information about JiWER can be found on [JiWER's PyPI page](https://pypi.org/project/jiwer/).
- **poster.pdf**
  - Poster presented at ICWSM'24.
- **License:** These additional resources are also released under a Creative Commons CC BY–NC-ND 4.0 International license.

For further details or questions related to the dataset or the study, please contact the lead author: Daniel J. Dubois at [d.dubois@northeastern.edu](mailto:d.dubois@northeastern.edu).
