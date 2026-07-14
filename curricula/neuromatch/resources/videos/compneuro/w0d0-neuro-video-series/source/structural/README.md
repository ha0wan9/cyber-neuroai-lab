# W0D0 Structural Notes and Key Slides

These bilingual structural notes are AI-generated drafts grounded in the corresponding timestamped caption summaries. Each note separates the instructional claim from interpretation, includes a key-slide guide, embeds the representative storyboard frames, and links to a full 10-second contact sheet.

The screenshots are extracted from YouTube's public storyboard service, so they are representative video frames rather than original-resolution stills.

| # | Video | Structural note | Key frames |
|---|---|---|---:|
| 01 | Intro | [Open](01-intro.structural.md) | 17 |
| 02 | Human Psychophysics | [Open](02-human-psychophysics.structural.md) | 20 |
| 03 | Behavioral Readout | [Open](03-behavioral-readout.structural.md) | 17 |
| 04 | Live in Lab | [Open](04-live-in-lab.structural.md) | 39 |
| 05 | Brain Signals: Spiking Activity | [Open](05-brain-signals-spiking-activity.structural.md) | 14 |
| 06 | Brain Signals: LFP | [Open](06-brain-signals-lfp.structural.md) | 11 |
| 07 | Brain Signals: EEG & MEG | [Open](07-brain-signals-eeg-meg.structural.md) | 15 |
| 08 | Brain Signals: fMRI | [Open](08-brain-signals-fmri.structural.md) | 19 |
| 09 | Brain Signals: Calcium Imaging | [Open](09-brain-signals-calcium-imaging.structural.md) | 15 |
| 10 | Stimulus Representation | [Open](10-stimulus-representation.structural.md) | 15 |
| 11 | Neurotransmitters | [Open](11-neurotransmitters.structural.md) | 10 |
| 12 | Neurons to Consciousness | [Open](12-neurons-to-consciousness.structural.md) | 15 |

## Reproduce

`../tools/extract-key-slides.py` retrieves and deduplicates storyboard frames. `../tools/generate-structural-notes.py` regenerates the bilingual structural note from the existing caption summaries and expects an Anthropic-compatible endpoint in the environment.
