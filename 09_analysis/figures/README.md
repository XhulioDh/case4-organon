# Figure data and scripts

The data behind the six figures in the report, and the scripts that rebuild it and draw the figures (appendix D.4).

## Files

| file | figure |
|---|---|
| `fig_s4_verdict_totals.csv`, `fig_s4_verdict_comparison.csv` | figure 1 (section 4): verdict totals, and the paired table behind the caption |
| `fig_s5_divergence_by_question.csv` | figure 2 (section 5; registered figure 1) |
| `fig_s6_reading_classifications.csv` | figure 3 (section 6) |
| `fig_s7_gender_assigned.csv` | figure 4 (section 7) |
| `fig_s8_lens_rates_predicted_observed.csv` | figure 5 (section 8; registered figure 2) |
| `fig_app_cofiring_counts.csv` | figure 6 (appendix E; registered figure 3) |
| `fig_app_cofiring_phi.csv` | the phi correlation for each pair of lenses; a record only, not drawn |

## Rebuilding

- `python3 figure_data_build.py <release folder> <output folder>` recomputes every CSV from `05_extraction/extraction_sheet.csv`, `05_extraction/run_order_and_pairing.csv` and `06_reading_sample/reading_sample.csv`. Its output is identical to the files here.
- `FIG_OUT=<output folder>/ python3 figure_draw.py` draws the six figures in `figures/` from these CSVs, as PNG (300 dpi) and SVG. It also draws two images made for announcing the case, which are not part of the report. It needs matplotlib and the TeX Gyre Heros font.

## Colours

Blue (#386fab) is thin and rust (#b25f38) is thick (Organon); grey is used for figures about pairs. Every mark carries a written label, so no figure depends on colour alone.
