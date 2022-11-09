    # begin
    #     open: = [Start];
    #     closed: = [];
    #     while open != [] do
    #         begin
    #             remove leftmost state from open, call it X;
    #             if X is a goal, return SUCCESS
    #                 else begin
    #                     generate children of X
    #                     put X on closed
    #                     discard children of X if already on open or closed;
    #                     put remaining children on left end of open
    #                 end
    #             end;
    #         return FAILURE
    #     end.