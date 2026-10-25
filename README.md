# PhotoSorter

An on-device tool that finds photos you probably want to delete and suggests
them for review. It never deletes anything on its own: you decide what goes.

Typical candidates are very blurry or very dark photos, as well as old
pictures of school material (worksheets, lecture slides, summaries), which
mostly contain a lot of text and are often several months old.

## Core Features

- Detect blurry photos
- Detect badly exposed photos (too dark, too bright or very low contrast)
- Detect text-heavy photos (mostly school-related)
- Combine any filter with a time range (e.g. "only photos older than 3 months")
- Review suggestions and delete selected photos in bulk (moved to trash)

## Bonus Features

- Find all photos of a specific person
- Find photos of specific objects (e.g. old shopping photos received via WhatsApp)

## Out of Scope

- Automatic deletion without user confirmation
- Cloud processing: all analysis runs locally on the device
- iOS (Android only for now)
- Videos

## Plan

1. Build a labeled dataset from my own photos (blurry / dark / text-heavy / keep)
2. Blur filter: implement and evaluate on the dataset
3. Darkness filter: implement and evaluate
4. Text filter (OCR or similar): implement and evaluate
5. Time range filter
6. Port the filters to an Android app
7. Publish the app (TBD: APK on GitHub or Play Store)
8. Bonus features

## Privacy

Photos and the dataset never leave the device and are not part of this
repository. Only code and evaluation metrics are published.

