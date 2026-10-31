# Shiruh

Open index.html for the subject picker. Chemistry is in chemistry.html; biology is in biology/index.html. Biology includes 56 chapters, 1,966 glossary terms and 168 original/adapted practice questions.

An interactive chemistry study guide adapted from the original Gen Chem Atlas source with permission confirmed by the site owner. Source and provenance are documented in SOURCE.md.

## Run locally

This is a static website with no build step or package dependencies. From this folder, run `python3 -m http.server 8000`, then open http://localhost:8000.

## Study

Open index.html through a local or authenticated web server. The original chapter navigation, notes, practice tests, flashcards, chemistry labs, periodic table and progress backup controls are retained.

## Add content

Open Content editor in the sidebar or visit editor.html. You can edit topic notes, terms, formulas and method steps; add topics; and add or edit choice, numerical and short-text questions.

Save each form. Changes save in this browser under `shiruh-content-v1`; reload the study guide to use them. Export content backup downloads your content JSON. Study progress is separate: export it from Settings in the study guide.

Download complete site exports a ZIP with the current content and all app files. Replace the files in your private repository with its contents to make your edits part of the source. Browser-local edits do not automatically update GitHub or other visitors.

The packaged default content is in content.js; content.json is a readable companion. If editing source JSON manually, update content.js from it using `python3 sync-content.py`. Changes in content.json alone are not loaded by the study interface.

## Privacy and hosting

Keep the GitHub repository private. The application has no built-in server authentication. Repository visibility and website access are separate: a private GitHub repository does not itself make a GitHub Pages website private. Do not enable public website deployment if visitors should need authorization. Use authenticated hosting or an eligible GitHub Enterprise Cloud private Pages deployment.

No automatic deployment workflow is included. Adding collaborators or publishing a site requires a separate, deliberate access configuration.

## Files

- index.html: original application and interactive chemistry labs, branded Shiruh.
- content.js: study dataset and local override validation.
- content.json: readable study dataset.
- editor.html / editor.js: content forms and backup/source exports.
- sync-content.py: update content.js from edited JSON.
- SOURCE.md: upstream provenance.
