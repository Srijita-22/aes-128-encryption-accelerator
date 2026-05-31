module rotword(
    input  wire [31:0] word_in,
    output wire [31:0] word_out
);

assign word_out = {
    word_in[23:16],
    word_in[15:8],
    word_in[7:0],
    word_in[31:24]
};

endmodule
