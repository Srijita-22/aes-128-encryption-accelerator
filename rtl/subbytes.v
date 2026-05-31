module subbytes (
    input  wire [7:0] data_in,
    output reg  [7:0] data_out
);

always @(*) begin
    case (data_in)
        8'h00: data_out = 8'h63;
        8'h01: data_out = 8'h7c;
        8'h02: data_out = 8'h77;
        8'h03: data_out = 8'h7b;
        8'h04: data_out = 8'hf2;
        8'h05: data_out = 8'h6b;
        8'h06: data_out = 8'h6f;
        8'h07: data_out = 8'hc5;

        // Continue filling from AES S-box table

        default: data_out = 8'h00;
    endcase
end

endmodule
