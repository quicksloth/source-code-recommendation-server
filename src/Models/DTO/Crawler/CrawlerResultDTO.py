from Models.DTO.Crawler.CrawlerCodeDTO import CrawlerCodeDTO


class CrawlerResultDTO(object):
    """
        Object that contains grouped all data of the code
    """

    def __init__(self, request_id, documentation, source_link):
        self.id = request_id
        self.source_link = source_link
        self.documentation = documentation if documentation else []
        self.codes = []

    def add_code(self, code):
        self.codes.append(code)

    def map_from_request(self, input_bus, result):
        for code_idx, code in enumerate(result.get('sourceCode')):
            # TODO: maybe extract ast in different threads
            ast = input_bus.code_extractor.extract_ast(code_text=code)

            # Handle error in case that ast cannot be parsed
            if not ast:
                continue

            libs = input_bus.code_extractor.extract_libs(ast)
            comments = input_bus.code_extractor.extract_comments(code, ast)
            variable_names = input_bus.code_extractor.extract_variables_names(ast)
            function_names = input_bus.code_extractor.extract_functions_names(ast)
            class_name = input_bus.code_extractor.extract_classes(ast)
            lines = input_bus.code_extractor.extract_number_of_lines(code_text=code)
            self.add_code(CrawlerCodeDTO(id=code_idx,
                                         libs=libs,
                                         comments=comments,
                                         variable_names=variable_names,
                                         function_names=function_names,
                                         class_name=class_name,
                                         lines_number=lines,
                                         code=code))
