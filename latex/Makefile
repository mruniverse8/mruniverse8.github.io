LATEX := pdflatex
NAME := ronaldo-franco-industry-cv
BUILD_DIR := build
PDF := $(BUILD_DIR)/$(NAME).pdf
SITE_PDF := ../assets/docs/$(NAME).pdf
LATEX_FLAGS := -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape

.PHONY: all install clean
.DELETE_ON_ERROR:

all: $(PDF)

$(PDF): $(NAME).tex Makefile
	mkdir -p $(BUILD_DIR)
	$(LATEX) $(LATEX_FLAGS) -output-directory=$(BUILD_DIR) $(NAME).tex
	$(LATEX) $(LATEX_FLAGS) -output-directory=$(BUILD_DIR) $(NAME).tex

install: $(PDF)
	cp $(PDF) $(SITE_PDF)

clean:
	rm -rf $(BUILD_DIR)
