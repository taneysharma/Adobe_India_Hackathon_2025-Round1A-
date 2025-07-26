# Adobe Hackathon – Round 1A: PDF Outline Extractor

##  Challenge Theme
**"Connecting the Dots Through Docs"**

Build a system that extracts a structured outline from a PDF document — identifying:
- The **title**
- Headings at different levels (**H1, H2, H3**)
- Page numbers

All output should be returned in a clean JSON format.

---

### 🛠️ Libraries Used

- **PyPDF2**  
  For reading and extracting text from PDF documents.

- **re**  
  Used for detecting heading patterns with regular expressions.

- **json**  
  Used to output structured data in a readable format.

- **datetime**  
  To timestamp the analysis for traceability.

- **pathlib**  
  For clean and portable file system operations.


##  Approach

1. **PDF Parsing**: Each page is read using `PyPDF2`.
2. **Text Extraction**: Text is split line-by-line.
3. **Title Detection**: The first well-formatted line is picked as the document title.
4. **Heading Detection**: Regex patterns are used to classify headings:
   - `H1`: ALL CAPS or prominent headers
   - `H2`: Two capitalized words (e.g., “System Design”)
   - `H3`: Numbered headings (e.g., “2.3 Background”)
5. **Output**: The structure is saved as a JSON file in the format:

```json
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "INTRODUCTION", "page": 1 },
    { "level": "H2", "text": "Problem Statement", "page": 2 },
    { "level": "H3", "text": "1.1 Scope", "page": 3 }
  ]
}
